import interfaces.CanCallable;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class RateLimiter {

    public static class SimpleRateLimiter implements CanCallable {
        Queue<Long> requests;
        int k;
        SimpleRateLimiter(int requestLimitInOneSecond) {
            requests = new ArrayDeque<>();
            k = requestLimitInOneSecond;
        }

        public boolean canCall() {
            long currentTime = System.currentTimeMillis();
            while (!requests.isEmpty() && requests.peek() < currentTime - 1000L) {
                requests.poll();
            }
            if (requests.size() >= k) {
                return false;
            }
            requests.offer(currentTime);
            return true;
        }
    }

    public static class SimpleRateLimiter2 implements CanCallable {
        int k;
        long[] counts;
        long cacheSum;
        long prevRequest;
        public SimpleRateLimiter2(int requestLimitInOneSecond) {
            counts = new long[requestLimitInOneSecond];
            k = requestLimitInOneSecond;
        }

        public boolean canCall() {
            long currentRequest = System.currentTimeMillis();
            clean(currentRequest);
            if (cacheSum >= k) {
                return false;
            }
            counts[(int) (currentRequest % k)] ++;
            cacheSum++;
            prevRequest = currentRequest;
            return true;
        }

        private void clean(long currentRequest) {
            if (currentRequest - prevRequest > 1000L) {
                cacheSum = 0;
                Arrays.fill(counts, 0);
                return;
            }

            for (long i = prevRequest + 1; i <= currentRequest; i++) {
                cacheSum -= counts[(int)(i % 1000)];
                counts[(int)(i % 1000)] = 0;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        SimpleRateLimiter rl1 = new SimpleRateLimiter(1000);
        testRateLimiter(rl1);
        SimpleRateLimiter2 rl2 = new SimpleRateLimiter2(1000);
        testRateLimiter(rl2);
    }

    public static void testRateLimiter(CanCallable c) {
        int callSuccess = 0;
        int callFailed = 0;
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 2000; i++) {
            if (c.canCall()) {
                callSuccess ++;
            } else {
                callFailed ++;
            }
        }
        long endTime = System.currentTimeMillis();
        System.out.println("Success " + callSuccess + " Failed: " + callFailed);
        System.out.println("Use: " + (endTime - startTime) + "ms");

    }
}
