package kmergen

import (
  "fmt"
  "strings"
)

func makemers (pos int, kmer []string, kmers map[string]int, alph []string, k int) map[string]int{
  for _, letter := range(alph) {
    kmer[pos] = letter

    if pos + 1 < k {
      makemers(pos + 1, kmer, kmers, alph, k)
    } else {
      done := strings.Join(kmer, "")
      kmers[done] = 0
    }
  }

  return kmers
}

func main () {
  pos := 0
  k := 5
  kmers := map[string]int{}
  kmer := make([]string, k)
  alphabet := "ACGT"

  alph := strings.Split(alphabet, "")
  kmers = makemers(pos, kmer, kmers, alph, k)

  fmt.Println(kmers)
}
