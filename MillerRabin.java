import java.util.*;

public class MillerRabin {
    private Random rand;
    private int iterations;
    private boolean composit;

    public MillerRabin(int n, int iterations) {
        rand = new Random();
        this.iterations = iterations;
        composit = false;

        primeTest(n);

    }
    
//RSA

    //millerRabinTest
    public boolean primeTest(int n) {

        
        if(n == 2 || n == 3) {
            return true;
        } else if (n <= 1 || n % 2 == 0) { //eftersom 0 och tal som är jämnt delbara är inte primtal
            return false;
        }
        
        int testPrime = n - 1;
        
        //Starta med exponenten 0
        int[] resultsOfFindingMandK = findMAndK(testPrime, 0);
        int m = resultsOfFindingMandK[0];
        int k = resultsOfFindingMandK[1];
        
        //Miller-rabinTest med många iterationer
        //a ska vara större än 2 men mindre än n-2

        for(int i = 0; i < iterations; i++) {
        int a =  2 + rand.nextInt(n-3);
            
        int x = (int) Math.pow(a, m) % n;
        
        if(x == 1 || x == n-1) {
            continue;
        }
            composit = true;

            for(int j = 0; j < k - 1; j++) {
                x = (int) Math.pow(2, a) % n;
                if(x == n-1) {
                    composit = false;
                    break;
                }
            } 
            //composit är den
        }

        return composit;
    }

    private int[] findMAndK(int m, int expAlsoKnownAsK) {
        if (m % 2 == 1) {  // Om m är udda, returnera m och k
            return new int[]{m, expAlsoKnownAsK};
        }
        return findMAndK(m / 2, expAlsoKnownAsK + 1); // Annars, fortsätt rekursivt dela med 2
        //och öka k tills vi har hittat de rätta m och k
    }
    

    //whole numbers vilket innbär integers enligt https://www.youtube.com/watch?v=qdylJqXCDGs
    // alltså k och m
    // algoritmen funkar genom att ta numret som vi vill ta reda på om det är primtal genom
    // Att använda Miller-Rabins primality test och funkar genom att ta numret N
    // ta det numret - 1 och dividerar det med 2 upphöjt med k
    // Tills det inte längre blir ett jämnt tal
    // m är det senaste talet dividerat med m
    // Vi kan använda oss av rekursiv metod

    //Nästa steg är att kontrollera att a är större än 1 och mindre än n-1
}

