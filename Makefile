CXX = clang++ 
CXXFLAGS = -Wall -std=C++14
SRC_DIR = src
OBJ_DIR = bin
OUT_FILE = main


#	defining the name of the output binary 
all: $(OUT_FILE)

#	defining the rule to generate the object files which need to be linked
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@ 

#	defining the rule to link the object files and create the final executable binary
$(OUT_FILE): $(OBJ_DIR)/*.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $(OBJ_DIR)/*.o -o $@




