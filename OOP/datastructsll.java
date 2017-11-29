import java.util.LinkedList;

 class datastructsll{

   public static void main(String[] args){

     LinkedList<String> colors = new LinkedList<String>();

     colors.add("Red");
     colors.add("Blue");
     System.out.println(colors);

     System.out.println(colors.contains("Red"));
     System.out.println(colors.size());


     try{
            colors.get(0);
            System.out.println(colors);
     }
     catch(Exception e){
       System.out.println("what");
     }

     for(String s: colors){
       System.out.println(s);
     }

     colors.clear();
     System.out.println(colors);


   }

}
