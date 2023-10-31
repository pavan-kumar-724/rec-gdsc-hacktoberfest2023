public class DuplicateElement {
       public static void main(String[] args) {  
       
        int [] arr = new int [] {1, 2, 3, 4, 2, 7, 8, 8, 3}; //creating and initialising an array
  
        System.out.println("Duplicate elements in given array: ");  
         
        for(int i = 0; i < arr.length; i++)
        {  //choosing an element sequentially
            for(int j = i + 1; j < arr.length; j++)
             {  //and checking with all the other items right to it
                if(arr[i] == arr[j])  //if equal, then it's a duplicate
                    System.out.println(arr[j]);  
            }  
        }  
    }  
}  
