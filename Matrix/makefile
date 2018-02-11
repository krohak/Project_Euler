
# The part below shall be uncomment and finished by you, add more lines as you need

#run_a2:
#a2: a2.out
#./a2.out < input.txt

 a2: a2.o Matrix.o Equation_solving.o
 	$(CXX) a2.o Matrix.o Equation_solving.o -o a2.out
 	
 a2.o: a2.cpp
 	$(CXX) -c $(CXXFLAGS) a2.cpp

 Equation_solving.o: Equation_solving.cpp Equation_solving.h
 	$(CXX) -c $(CXXFLAGS) Equation_solving.cpp

 # The part above shall be uncomment and finished by you

 Matrix.o: Matrix.cpp Matrix.h
 	$(CXX) -c $(CXXFLAGS) Matrix.cpp
