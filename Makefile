CXX = g++
CXXFLAGS = ``
SOURCES = main.cc
EXEC = test

build:
	@$(CXX) $(SOURCES) $(CXXFLAGS) -o $(EXEC).o
	@clear
	@./$(EXEC).o
