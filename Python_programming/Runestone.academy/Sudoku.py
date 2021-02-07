# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:50:11 2021

@author: Komputer
"""

class Sudoku:
    
    def __init__(self,sudoku):
        self.sudoku=sudoku
        
    def findFirstEmtpy(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j]==0:
                    return i,j
        return -1,-1        
                
    def printsudoku(self):
        print("\n")
        for i in range(len(self.sudoku)):
            line = ""
            if i == 3 or i == 6:
                print("---------------------")
            for j in range(len(self.sudoku[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += str(self.sudoku[i][j])+" "
            print(line)
            
    def Validation_check(self,i,j,element):
        
        #check row
        for k in range(9):
            if k==j:
                continue
            else:
                if self.sudoku[i][k]==element:
                    return False
                
        for l in range(9):
            if l==i:
                continue
            else:
                if self.sudoku[l][j]==element:
                    return False
        
        minX=3*(i//3)
        minY=3*(j//3)
        for p in range(minX,minX+3):
            for q in range(minY,minY+3):
                if p==i and q==j:
                    continue
                if self.sudoku[p][q]==element:
                   return False
         
        return True
        
        #check column
        # check box
        

    def solve_sudoku(self):
        i,j=self.findFirstEmtpy()
        if i==-1:
            return True
        else:
            for element in range(1,10):
                is_valid=self.Validation_check(i,j,element)
                if is_valid==True:
                    self.sudoku[i][j]=element
                    if self.solve_sudoku():
                        return True
                    self.sudoku[i][j]=0
            
            return False
                   
                        

if __name__=="__main__":
     
    sudoku_example = [
        [8,1,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]
    
    sudoku= Sudoku(sudoku_example)
    if(sudoku.solve_sudoku()):
        sudoku.printsudoku()
    else:
        print("Solution doesn't exists")
