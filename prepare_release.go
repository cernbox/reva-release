// Copyright 2018-2023 CERN
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// In applying this license, CERN does not waive the privileges and immunities
// granted to it by virtue of its status as an Intergovernmental Organization
// or submit itself to any jurisdiction.

package main

import (
	"bufio"
	"bytes"
	"errors"
	"flag"
	"fmt"
	"io"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

var (
	author           = flag.String("author", "", "the author that creates the release")
	email            = flag.String("email", "", "the email of the author that creates the release")
	versionTag       = flag.String("version-tag", "", "the tag of the version")
	version          = flag.String("version", "0", "version to tag")
	revaVersion      = flag.String("reva-version", "", "the reva version and commit")
	releaseCandidate = flag.Bool("release-candidate", false, "Is a release candidate?")
)

const (
	specFile   = "cernbox-revad.spec"
	prodBranch = "cernbox"
)

func init() {
	flag.Parse()

	if *author == "" || *email == "" || *revaVersion == "" {
		fmt.Fprintln(os.Stderr, "fill the author, email, and revaVersion flags")
		os.Exit(1)
	}
}

func main() {
	err := releaseNewVersion(*author, *email, *revaVersion)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func releaseNewVersion(author, email, revaVersion string) error {
	specContent, err := readSpecFile()
	if err != nil {
		return fmt.Errorf("error reading spec content: %w", err)
	}

	versionStr, err := getNextVersion(specContent)
	fmt.Printf("Version is %s\n", versionStr)
	if err != nil {
		return err
	}
	if *versionTag != "" && *versionTag != prodBranch {
		versionStr += "." + *versionTag
	}

	// update the version in the spec file
	for i, line := range specContent {
		if strings.HasPrefix(line, "Version:") {
			specContent[i] = "Version: " + versionStr
		}
	}

	// add the changelog
	changelogHeader := -1
	for i, line := range specContent {
		if strings.HasPrefix(line, "%changelog") {
			changelogHeader = i
		}
	}

	if changelogHeader == -1 {
		return errors.New("changelog header not found in spec file")
	}

	var newChangelog []string
	today := time.Now().Format("Mon Jan 02 2006")
	newChangelog = append(newChangelog, fmt.Sprintf("* %s %s <%s> %s", today, author, email, versionStr))
	newChangelog = append(newChangelog, fmt.Sprintf("- v%s, based on %s", versionStr, revaVersion))

	var newSpec []string
	newSpec = append(newSpec, specContent[:changelogHeader+1]...)
	newSpec = append(newSpec, newChangelog...)
	newSpec = append(newSpec, specContent[changelogHeader+1:]...)

	err = writeSpecFile(newSpec)
	if err != nil {
		return fmt.Errorf("error updating spec file: %w", err)
	}

	return nil
}

func readSpecFile() ([]string, error) {
	f, err := os.Open(specFile)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	scan := bufio.NewScanner(f)

	var spec []string
	for scan.Scan() {
		spec = append(spec, scan.Text())
	}

	return spec, nil
}

func writeSpecFile(spec []string) error {
	f, err := os.OpenFile(specFile, os.O_WRONLY|os.O_TRUNC, 0644)
	if err != nil {
		return err
	}
	defer f.Close()

	for _, line := range spec {
		f.WriteString(line + "\n")
	}

	return nil
}

func getNextVersion(spec []string) (string, error) {
	if *version != "0" {
		return *version, nil
	}
	rcversion := int64(0)
	for _, line := range spec {
		if strings.HasPrefix(line, "Version:") {
			v := strings.TrimPrefix(line, "Version: ")
			if strings.Contains(v, "_rc") {
				var err error
				splitrc := strings.Split(v, "_rc")
				rcversion, err = strconv.ParseInt(splitrc[1], 10, 64)
				if err != nil {
					return "", err
				}
				v = splitrc[0]
				fmt.Printf("Previous version has _rc, of which actual version is %s\n", v)
			}
			split := strings.Split(v, ".")

			ver, err := strconv.ParseInt(split[2], 10, 64)
			if err != nil {
				return "", err
			}
			fmt.Printf("Release candidate? %t\n", *releaseCandidate)
			if *releaseCandidate {
				// We want x.y.z_rc(a)
				if rcversion == 0 {
					return fmt.Sprintf("%s.%s.%d_rc%d", split[0], split[1], int(ver)+1, int(rcversion)+1), nil
				}
				return fmt.Sprintf("%s.%s.%d_rc%d", split[0], split[1], int(ver), int(rcversion)+1), nil
			}
			if rcversion != 0 { // previous version was x.y.z_rc(a), so now we just want x.y.z
				return fmt.Sprintf("%s.%s.%d", split[0], split[1], int(ver)), nil
			}
			return fmt.Sprintf("%s.%s.%d", split[0], split[1], int(ver)+1), nil
		}
	}
	panic("cannot find a version")
}

func run(cmd *exec.Cmd) {
	var b bytes.Buffer
	mw := io.MultiWriter(os.Stdout, &b)
	cmd.Stdout = mw
	cmd.Stderr = mw
	err := cmd.Run()
	if err != nil {
		fmt.Println("ERROR: ", err.Error())
		os.Exit(1)
	}
}
