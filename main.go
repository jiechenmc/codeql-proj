package main

import "fmt"

type ServerlessYaml struct {
	Inputs struct {
		Src struct {
			Src      string `yaml:"src"`
		}
	}
}


func main() {
	fmt.Println("Main.go")
}