import java.math.BigInteger;
import java.util.Random;

public class algorithmTest {
    private static final int BITS = 512;
    private static final int ITERATIONS = 1000;
    private static final Random random = new Random();

    public static BigInteger generateRandomLargeBit(int bits) {
        return new BigInteger(bits, random);
    }

    public static double firstAlgorithm(BigInteger n, int iterations) {
        BigInteger x = new BigInteger(n.bitLength() - 1, random).mod(n.subtract(BigInteger.TWO)).add(BigInteger.TWO);
        long startTime = System.nanoTime();
        
        for (int i = 0; i < iterations; i++) {
            x = x.modPow(BigInteger.TWO, n);
        }

        long endTime = System.nanoTime();
        long timeForAlgorithm = endTime - startTime;
        return timeForAlgorithm/1e9; 
    }

    public static double secondAlgorithm(BigInteger n, int iterations) {
        BigInteger a = new BigInteger(n.bitLength() - 1, random).mod(n.subtract(BigInteger.TWO)).add(BigInteger.TWO);
        BigInteger m = new BigInteger(n.bitLength() - 1, random).mod(n.subtract(BigInteger.ONE)).add(BigInteger.ONE);
        int j = random.nextInt(101); // random siffra mellan 1 och 100

        long startTime = System.nanoTime();
        
        for (int i = 0; i < iterations; i++) {
            BigInteger exp = BigInteger.TWO.pow(j).multiply(m);
            a.modPow(exp, n);
        }
        
        long endTime = System.nanoTime();
        long timeForAlgorithm = endTime - startTime;
        return timeForAlgorithm/1e9; 
    }

    public static double compareAlgorithm() {
            BigInteger n = generateRandomLargeBit(BITS);
            double timeForFirstAlgorithm = firstAlgorithm(n, ITERATIONS);
            double timeForSecondAlgorithm = secondAlgorithm(n, ITERATIONS);
    
            if (timeForFirstAlgorithm < timeForSecondAlgorithm) {
                //System.out.println("First algorithm is faster:");
                //System.out.println(timeForSecondAlgorithm - timeForFirstAlgorithm);
                return timeForFirstAlgorithm;
            } else {
                //System.out.println("Second algorithm is faster:");
                //System.out.println(timeForFirstAlgorithm - timeForSecondAlgorithm);
                return timeForSecondAlgorithm;
            }
        }
    
        public static void getAverageTime() {
            double total = 0;
            for (int i = 0; i < 100; i++) {
                total += compareAlgorithm();
        }
        System.out.println("Average time: " + (total / 100));
    }

    public static void main(String[] args) {
        //compareAlgorithm();
        getAverageTime();
    }
}