import java.util.*;

class CustomCipher {
    // This function repeats the key in a cyclic manner to match the length of the Plaintext
    static String generateKey(String str, String key)
    {
        int x = str.length();
    
        for (int i = 0; ; i++)
        {
            if (x == i)
                i = 0;
            if (key.length() == str.length())
                break;
            key+=(key.charAt(i));
        }
        return key;
    }
    
    // Encryption
    static String Encrypt(String str, String key)
    {
        String ciphertext="";
        int arr[] = new int[str.length()];
        
        
        for (int i = 0; i < str.length(); i++)
        {
            // Encryption formula
            int x = ((str.charAt(i)-'A') ^ (key.charAt(i)-'A'));
            
            // convert into alphabets(ASCII) and add to string
            x += 'A';                  
            ciphertext+=(char)(x);
        }
        return ciphertext;
    }
    
    // Decryption
    static String Decrypt(String ciphertext, String key)
    {
        String plaintext="";
    
        for (int i = 0 ; i < ciphertext.length() && 
                                i < key.length(); i++)
        {
             // Decryption formula
            int x = ((ciphertext.charAt(i)-'A') ^ (key.charAt(i)-'A'));
    
            // convert into alphabets(ASCII) and add to string
            x += 'A';
            plaintext+=(char)(x);
        }
        return plaintext;
    }
    
    static String LowerToUpper(String s)
    {
        StringBuffer str =new StringBuffer(s); 
        for(int i = 0; i < s.length(); i++)
        {
            if(Character.isLowerCase(s.charAt(i)))
            {
                str.setCharAt(i, Character.toUpperCase(s.charAt(i)));
            }
        }
        s = str.toString();
        return s;
    }
    
    
    
    // Main
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
            
        System.out.print("\n Enter PlainText - ");
    	String Str = sc.nextLine();
    	
    	System.out.print(" Enter Keyword   - ");
    	String Keyword = sc.nextLine();
    	
        // String Str = "This is a Secret Message";
        // String Keyword = "Secret";
         
        String str = LowerToUpper(Str);
        String keyword = LowerToUpper(Keyword);
    
        String key = generateKey(str, keyword);
        String cipherText = Encrypt(str, key);
    
        System.out.println("\n Encrypted text  - " + cipherText);
        System.out.println(" Decrypted text  - " + Decrypt(cipherText, key));
            
        sc.close();
            
    }
}
