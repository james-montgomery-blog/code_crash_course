# Go

## History

Golang (Go), like Rust, is an attempt to get the performance of C/C++ with modern features like memory safety. Go is a great language when efficient concurrency is a project requirement but the developers want to keep the code base simple and elegant. Go first appeared in 2009.

## Installation

```
mkdir $HOME/Go
mkdir -p $HOME/Go/src/github.com/user
export GOPATH=$HOME/Go
export GOROOT=/usr/local/opt/go/libexec
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
brew install go
go get golang.org/x/tools/cmd/godoc
```

## HellowWorld

Run without compiling.

```
cd ./HelloWorld
go run HelloWorld.go
cd ..
```

Run with compiling.

```
cd ./HelloWorld
go build HelloWorld.go
./HelloWorld
cd ..
```
