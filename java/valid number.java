class Solution {
    public boolean isNumber(String s) {
        s = s.trim();

        boolean seenDigit = false;
        boolean seenDot = false;
        boolean seenExp = false;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                seenDigit = true;
            }

            else if (c == '+' || c == '-') {
                // only valid at start OR after e/E
                if (i > 0 && s.charAt(i - 1) != 'e' && s.charAt(i - 1) != 'E') {
                    return false;
                }
            }

            else if (c == '.') {
                // dot only once & before exponent
                if (seenDot || seenExp) return false;
                seenDot = true;
            }

            else if (c == 'e' || c == 'E') {
                // must have digit before and only once
                if (seenExp || !seenDigit) return false;
                seenExp = true;
                seenDigit = false; // reset for exponent part
            }

            else {
                return false;
            }
        }

        return seenDigit;
    }
}
