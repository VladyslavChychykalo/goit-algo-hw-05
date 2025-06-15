import timeit

# === Алгоритми пошуку ===
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return True
    bad_char = {pattern[i]: i for i in range(m)}
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return True
        s += max(1, j - bad_char.get(text[s + j], -1))
    return False

def rabin_karp_search(text, pattern):
    d, q = 256, 101
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p = t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(n - m + 1):
        if p == t and text[s:s+m] == pattern:
            return True
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return False

# === Час виконання ===
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)

# === Завантаження текстів ===
with open("стаття_1.txt", mode="r", encoding="utf-8", errors="replace") as f:
    text1 = f.read()
with open("стаття_2.txt", mode="r", encoding="utf-8", errors="replace") as f:
    text2 = f.read()

# === Підрядки ===
existing = "структури даних"
not_existing = "qwerty"

# === Пошук ===
algorithms = {
    "KMP": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search
}

print(f"{'Алгоритм':<15} | {'Text1 існує':<12} | {'Text1 нема':<12} | {'Text2 існує':<12} | {'Text2 нема':<12}")
print("-" * 65)
for name, func in algorithms.items():
    t1_yes = measure_time(func, text1, existing)
    t1_no = measure_time(func, text1, not_existing)
    t2_yes = measure_time(func, text2, existing)
    t2_no = measure_time(func, text2, not_existing)
    print(f"{name:<15} | {t1_yes:<12.6f} | {t1_no:<12.6f} | {t2_yes:<12.6f} | {t2_no:<12.6f}")
