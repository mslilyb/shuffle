package main

import (
  "bufio"
  "flag"
  "fmt"
  "os"
  "strconv"
  "strings"
)

type Feature struct {
  Chr string
  Beg int
  End int
}

//This should probably be a switch-case statement, but its functionally the same
func overlap(f1 *Feature, f2 *Feature) bool {
  if f2.Beg <= f1.End && f2.End >= f1.Beg{
      return true
  } else {
      return false
  }

}


type State_Iterator struct {
  scanner *bufio.Scanner
  filehandle *os.File
  current *Feature
  done bool
}

func (si *State_Iterator) Element() *Feature {
  return si.current
}

func (si *State_Iterator) next() bool {

  if si.scanner.Scan() {
    line := si.scanner.Text()
    c := strings.Fields(line)

    si.current.Chr = c[0]
    si.current.Beg, _ = strconv.Atoi(c[1])
    si.current.End, _ = strconv.Atoi(c[2])

    return true

  } else {
    si.filehandle.Close()
    return false
  }

}

func readfile (fn string) *State_Iterator{


  fh, err := os.Open(fn)

  if err!= nil {
    panic(err)
  }

  si := new(State_Iterator)
  si.current = new(Feature)
  si.done = false
  si.filehandle = fh
  si.scanner = bufio.NewScanner(fh)

  return si
}


func main () {
  var fname1, fname2 string

  flag.StringVar(&fname1, "f1", "", "path to first file")
  flag.StringVar(&fname2, "f2", "", "path to second file")

  flag.Parse()

  file1si := readfile(fname1)
  file2si := readfile(fname2)

  file1 := make([]*Feature, 10)
  file2 := make([]*Feature, 10)
  i,j := 0,0

  for file1si.next() {
    e := file1si.Element()
    fmt.Println(e, " ", file1)
    file1[i] = e
    i++
  }

  for file2si.next() {
      e := file1si.Element()
      fmt.Println(e, " ", file2)
      file2[j] = e
      j++
    }


  fmt.Println(file1, file2)

  for _, feature1 := range file1 {
    fmt.Println(*feature1)
    /*for _, feature2 := range file2 {
      if overlap(feature1, feature2) {
        fmt.Println(*feature1, " ", *feature2)*/
      }
    }
