class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        begin = end = 0
        min_len = None
        result = ""
        m = {}
        for c in t:
            m[c] = m[c] + 1 if c in m else 1
        # print(m)
        counter = len(t)

        while end < len(s):
            if s[end] in m:
                if m[s[end]] > 0:
                    counter -= 1
                m[s[end]] -= 1

            while counter == 0:
                # print(end)
                if min_len == None or end - begin < min_len:
                    min_len = end - begin
                    # print("{},{}".format(begin, end))
                    result = s[begin:end + 1]

                if begin <= end and s[begin] in m:
                    m[s[begin]] += 1
                    if m[s[begin]] > 0:
                        counter += 1

                begin += 1

            end += 1
        return result

"""
// Java version:
public class Solution {
    public String minWindow(String S, String T) {
        int[] map = new int[128];
		//System.out.println(map[0]);

		int counter = T.length(), begin = 0, end = 0, minLen = Integer.MAX_VALUE;
		int head = 0;
		for (int i = 0; i < T.length(); i++)
			map[T.charAt(i)] ++;

		//System.out.println(map['b']);

		while(end < S.length()){

			if(map[S.charAt(end)] > 0){
				counter--;
			}
			map[S.charAt(end)]--;
			end++;

			while (counter == 0){
				if(end - begin < minLen){
					head = begin;
					minLen = end - begin;
				}
				if (map[S.charAt(begin)] == 0){
					counter++;
				}
				map[S.charAt(begin)]++;
				begin++;
			}
		}
		return minLen == Integer.MAX_VALUE ? "" : S.substring(head, head + minLen);

    }
}
"""
