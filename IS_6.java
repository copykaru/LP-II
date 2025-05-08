
import java.math.BigInteger;
import java.util.Random;

public class IS_6 {

    // Method to calculate (base^exponent) % mod
    public static BigInteger powerMod(BigInteger base, BigInteger exponent, BigInteger mod) {
        return base.modPow(exponent, mod);
    }

    public static void main(String[] args) {
        // Global public elements: prime number q and primitive root a
        BigInteger q = new BigInteger("23");  // A small prime number
        BigInteger a = new BigInteger("5");  // A primitive root of q

        // Alice and Bob select their private keys
        BigInteger alicePrivateKey = new BigInteger("4");  // Alice's private key
        BigInteger bobPrivateKey = new BigInteger("3");   // Bob's private key

        // Calculate public keys
        BigInteger alicePublicKey = powerMod(a, alicePrivateKey, q);
        BigInteger bobPublicKey = powerMod(a, bobPrivateKey, q);

        System.out.println("Alice's public key: " + alicePublicKey);
        System.out.println("Bob's public key: " + bobPublicKey);

        // Alice and Bob exchange public keys and calculate shared secret key
        BigInteger aliceSharedKey = powerMod(bobPublicKey, alicePrivateKey, q);
        BigInteger bobSharedKey = powerMod(alicePublicKey, bobPrivateKey, q);

        System.out.println("Alice's shared key: " + aliceSharedKey);
        System.out.println("Bob's shared key: " + bobSharedKey);

        // The shared keys should be the same
        if (aliceSharedKey.equals(bobSharedKey)) {
            System.out.println("The shared secret key is: " + aliceSharedKey);
        } else {
            System.out.println("The keys do not match. There was an error.");
        }
    }
}