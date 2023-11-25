def submatrix(matrix, row, col): #return submatrix by removing specified row/column
  # uses list comp. to iterate over rows to create new matrix
  return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def determinant(matrix):
  n = len(matrix) # Get matrix size 

  # Base case: determinant of a 1x1 matrix is the element itself
  if n == 1:
      return matrix[0][0]

  det = 0
  #Loop over each column of first row to calc determinant 
  for col in range(n):
      sign = (-1) ** col # Sign based on column index 
    # Calculate the contribution of current element to the determinant
      det += sign * matrix[0][col] * determinant(submatrix(matrix, 0, col))

  return det

def main():
  n = int(input("Enter the size of the square matrix (n): ")) # Size input 

  # Input matrix
  print("Enter the entries of the matrix (row-wise):")
  matrix = [list(map(int, input().split())) for _ in range(n)]

  # Compute determinant
  det_value = determinant(matrix)

  # Display the result with proper format 
  print(f"The determinant of the matrix is: {det_value}")

if __name__ == "__main__":
  main()