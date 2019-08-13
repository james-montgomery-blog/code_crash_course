CC=gcc
CFLAGS=-Wall -Wextra -Wpedantic -g # compile commdans -Werrors
DEPS = ./src/utils.h
OBJ = ./src/main.o
LIBS =-lcblas -I/usr/local/include
.PHONY: all

all: main

%.o: %.c $(DEPS)
	$(CC) -c -o $(LIBS) $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)
