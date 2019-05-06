// 15/04/2019
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var morseAlphabet = map[string]rune{
	".-":   'A',
	"-...": 'B',
	"-.-.": 'C',
	"-..":  'D',
	".":    'E',
	"..-.": 'F',
	"--.":  'G',
	"....": 'H',
	"..":   'I',
	".---": 'J',
	"-.-":  'K',
	".-..": 'L',
	"--":   'M',
	"-.":   'N',
	"---":  'O',
	".--.": 'P',
	"--.-": 'Q',
	".-.":  'R',
	"...":  'S',
	"-":    'T',
	"..-":  'U',
	"...-": 'V',
	".--":  'W',
	"-..-": 'X',
	"-.--": 'Y',
	"--..": 'Z',
	"/":    ' ',
}

func main() {
	var translated strings.Builder

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	fmt.Print(">> ")
	for i := 0; scanner.Scan(); i++ {
		translated.WriteRune(morseAlphabet[scanner.Text()])
	}

	fmt.Println(translated.String())
}
