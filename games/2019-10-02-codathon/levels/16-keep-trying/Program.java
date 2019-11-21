public class Program {
    public static void main(String[] args) {
        String hash = "uq89:8dkE(psd|5wp";
        String input = args[0];
        if(input.length() != hash.length()) {
            System.out.println("Keep Trying!");
            System.exit(1);
        }

        String changed = change(input);
        
        if(changed.equals(hash)) {
            System.out.println("CTF{" + input + "}");
        } else {
            System.out.println("Keep Trying!");
            System.exit(1);
        }
    }

    private static String change(String s) {
        char[] temp = new char[s.length()];
        for(int i = 0; i < s.length(); i++) {
            temp[i] = (char)(s.charAt(i) + 5);
        }
        return new String(temp);
    }
}