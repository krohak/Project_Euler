import java.util.LinkedHashSet;
//import java.util.HashSet;

 class datastructset{

   public static void main(String[] args){

     LinkedHashSet<String> colors = new LinkedHashSet<String>();

     colors.add("Red");
     colors.add("Blue");
     System.out.println(colors);

     System.out.println(colors.contains("Red"));
     System.out.println(colors.size());


     try{
            //colors.get(1);
            System.out.println(colors);
     }
     catch(Exception e){
       System.out.println("what");
     }

     /*for(String s, Integer i: colors){
       System.out.println(s);
     }*/

     colors.clear();
     System.out.println(colors);


   }

}
