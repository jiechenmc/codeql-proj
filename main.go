package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/goccy/go-yaml"
)

type Serverless struct {
	Functions map[string]struct {
		Handler string `yaml:"handler"`
	} `yaml:"functions"`
}

func main() {
	data, err := os.ReadFile("lambda/serverless.yml")
	if err != nil {
		panic(err)
	}
	var cfg Serverless
	if err := yaml.Unmarshal(data, &cfg); err != nil {
		panic(err)
	}

	handler_cfg := strings.Split(cfg.Functions["hello"].Handler, ".")

	file, function := handler_cfg[0], handler_cfg[1]

	fmt.Println("Handler for 'hello':", file, function)


}
