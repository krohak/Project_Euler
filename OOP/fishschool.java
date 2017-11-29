 class fishschool{

   public static void main(String[] args){

     Fish f = new Fish();
     Fish f2 = new Fish();
     System.out.println(f.getFin());
     f2.setFin(9);
     System.out.println(f.getFin());
     System.out.println(f2.getFin());
     System.out.println(Fish.getFishInstances());

    // System.out.println(no);

     Shark s1 = new Shark(92);
     System.out.println(s1.getTeeth());
     System.out.println(s1.getFin());
     s1.swim_backwards();

     Clownfish c1 = new Clownfish();
     c1.swim();
     c1.swim(1,4);

     f2.setFin(4);
     System.out.println(f.equals(f2));
     

     //System.gc();


   }






}
