CC=gcc
CFLAGS=-Wall -Wextra -Wpedantic -g
BIN=matrix
BUILD=build
SRC=src
SOURCES=$(wildcard $(SRC)/*.c)
OBJECTS = $(patsubst $(SRC)/%.c,$(BUILD)/%.o,$(SOURCES))

dir_guard = @mkdir -p $(@D)

all : $(BUILD)/$(BIN)

run: all
	$(info running...)
	./${BUILD}/${BIN}

debug: all
	gdb $(BUILD)/$(BIN)

$(BUILD)/$(BIN): $(OBJECTS)
	$(dir_guard)
	$(CC) $^ -o $@ -lblas

$(BUILD)/%.o: $(SRC)/%.c
	$(dir_guard)
	$(CC) -c $(CFLAGS) $< -o $(BUILD)/$(@F)

.PHONY: clean all debug run

clean:
	rm -rf $(BUILD)
