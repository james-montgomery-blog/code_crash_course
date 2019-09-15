# Go

## History

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
