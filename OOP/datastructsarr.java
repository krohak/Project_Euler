import java.util.ArrayList;

 class datastructsarr{

   public static void main(String[] args){

     ArrayList<String> colors = new ArrayList<String>();

     colors.add("Red");
     System.out.println(colors);

     System.out.println(colors.contains("Red"));
     System.out.println(colors.size());


     try{
            colors.get(2);
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
