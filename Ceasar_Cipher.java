package CNS_Assignments;

import java.util.*;
import java.io.*;
import java.net.*;


public class Ceasar_Cipher {

	public static String ceasarEncrypt(String plaintext, int key) {
		String ciphertext = "";
		int n = plaintext.length();
		char ch;
		
		for(int i=0; i<n; i++) {
			ch = plaintext.charAt(i);
			ch+=key;
			ciphertext+=ch;
		}
		
		return ciphertext;
	}
	
	public static void writeToFile(String data, String filename) {
		try {
	        OutputStream out = new FileOutputStream(filename);
	        byte[] dataBytes = data.getBytes();									// Converts the string into bytes
	        out.write(dataBytes);											    // Writes data to the output stream
	        
	        System.out.println("Data is written to the " + filename + " file.");
	        out.close();		            									// Closes the output stream
	    
		}
        catch (Exception e) {
            e.getStackTrace();
        }

	}

	
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);

		try {
    		System.out.print("Enter PlainText: ");
    		String plainText = in.nextLine();
    		
    		System.out.print("Enter Key: ");
    		int key = in.nextInt();
    		String keyString = Integer.toString(key);
    		
    		String cipherText = ceasarEncrypt(plainText, key);
    		
    		writeToFile(cipherText, "output.txt");
    		writeToFile(keyString, "key.txt");
           
        }

        catch (Exception e) {
            e.getStackTrace();
        }
	
		in.close();
	}

}
