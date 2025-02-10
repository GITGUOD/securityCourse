public class Main {
    public static void main(String[] args) {

        //Vi behöver iterationer för att testa olika på a värden för att verkligen se om talet n är ett primtal
        int iterations = 10;
        int n = 53;
        MillerRabin mr = new MillerRabin(n, iterations);
        System.out.println(mr);
    }
}
