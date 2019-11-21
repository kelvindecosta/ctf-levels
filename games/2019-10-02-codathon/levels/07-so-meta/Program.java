public class Program {
    public static void main(String[] args) {
        try {
            String clsName = args[0].substring(0, args[0].length() - 6);
            Class cls = Class.forName(clsName);
            Program obj = (Program) cls.newInstance();
            System.out.println(obj.flag());
        } catch(Exception e) {
            System.out.println("That's not the right file!");
        }
    }

    String flag(){
        return "CTF{53lf_r3f3r3n714l}";
    }
}