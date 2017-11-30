import java.util.ArrayList;
import java.util.Collections;

import java.util.Iterator;

 class datastructsarr{

   public static void main(String[] args){

     ArrayList<String> colors = new ArrayList<String>();

     colors.add("Red");
     colors.add("Blue");
     System.out.println(colors);

     System.out.println(colors.contains("Red"));
     System.out.println(colors.size());


     try{
            colors.get(2);
     }
     catch(Exception e){
       System.out.println("what");
     }

     Collections.sort(colors);
     //System.out.println(Collections.binarySearch(colors,"Red"));

     /*for(String s: colors){
       System.out.println(s);
     }*/

     Iterator <String> it = colors.iterator();
     while(it.hasNext()){
     System.out.println(it.next());}

     colors.clear();
     //System.out.println(colors);


   }

}
