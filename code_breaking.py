import hashlib

hashes_map = {
    "7c4a8d09ca3762af61e59520943dc26494f8941b": 1,
    "dea742e166979027ae70b28e0a9006fb1010e760": 2,
    "789d1dd349b28fcdb61da280d58c0df721da9143": 3,
    "f122778ac920da565c668acc6c0a247edd6adb27": 4,
    "8aefb06c426e07a0a671a1e2488b4858d694a730": 5,
    "ad8167df4b75bd9f2e165ea9f6053195cf7652b5": 6,
    "ea074a4e069fdd30468ad32019334091cd6f2545": 7,
    "754f1d6a31e8fcfc30cf8257d9e035a92a11b328": 8,
    "1db7b321af0e8d0da63277a9d0bc67a176b03ed8": 9,
    "d1808c6fc5dd939a1889da7c11f68bdb10b727b7": 10,
    "b7c71d5a119e91a42a9abd1fcb02692a28c404d4": 11,
    "ca1f7fef6f7a839c083e96f77ac7cf3991323af7": 12,
    "39fb6e0d23f83a4e016c0f725dda9050b72af4a2": 13,
    "08958bb5e582136f7b4cc32bdbe9b23603613d1a": 14,
    "177080c8b8f44ea62c1a4baeeeb726ac1f9985ae": 15,
    "808543b37169708c597e23c7adbe743be8e05ad7": 16,
    "9a4b9040cb885c4c25db1d821a2cec35c11cd636": 17,
    "925184f33c2cb6f0bb7abdfeef317001d2569051": 18,
    "65abe9e1efbd6efbdf3d6ea3c4c2f6c0325cbb68": 19,
    "13de3541c0564ee2267e37a85045a615476cfa03": 20,
}


# single word hassh
def method_1():
    with open("dictionary.txt", "r") as file:
        for line in file:
            word = line.strip()

            computed_hash = hashlib.sha1(word.encode()).hexdigest()

            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")


# numeric attempts ============
# single digit
def method_1_digit():
    for i in range(10):
        word = f"{i:01d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 1 digit")


# double digit
def method_2_digit():
    for i in range(100):
        word = f"{i:02d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 2 digit")


# triple digit
def method_3_digit():
    for i in range(1000):
        word = f"{i:03d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 3 digit")


# 4 digit
def method_4_digit():
    for i in range(10000):
        word = f"{i:04d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 4 digit")


# 5 digit
def method_5_digit():
    for i in range(100000):
        word = f"{i:05d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 5 digit")


# 6 digit
def method_6_digit():
    for i in range(1000000):
        word = f"{i:06d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 6 digit")


# 7 digit
def method_7_digit():
    for i in range(10000000):
        word = f"{i:07d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 7 digit")


# 8 digit
def method_8_digit():
    for i in range(100000000):
        word = f"{i:08d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 8 digit")


# 9 digit
def method_9_digit():
    for i in range(1000000000):
        word = f"{i:09d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 9 digit")


# 10 digit
def method_10_digit():
    for i in range(10000000000):
        word = f"{i:010d}"
        computed_hash = hashlib.sha1(word.encode()).hexdigest()
        if computed_hash in hashes_map:
            match_num = hashes_map[computed_hash]
            print(f"Match found: Hash #{match_num} {word} -> {computed_hash}")
    print("Done with method 10 digit")


# === Single Word + up to 5 digits
# Single word + 1 digit (
def method_word_plus_1_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    for word in words:
        for i in range(10):
            candidate = f"{word}{i:01d}"
            computed_hash = hashlib.sha1(candidate.encode()).hexdigest()
            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
    print("Done with Single word + 1 digit")


# Single word + 2 digits
def method_word_plus_2_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    for word in words:
        for i in range(100):
            candidate = f"{word}{i:02d}"
            computed_hash = hashlib.sha1(candidate.encode()).hexdigest()
            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
    print("Done with Single word + 2 digit")


# Single word + 3 digits
def method_word_plus_3_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    for word in words:
        for i in range(1000):
            candidate = f"{word}{i:03d}"
            computed_hash = hashlib.sha1(candidate.encode()).hexdigest()
            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
    print("Done with Single word + 3 digit")


# Single word + 4 digits
def method_word_plus_4_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    for word in words:
        for i in range(10000):
            candidate = f"{word}{i:04d}"
            computed_hash = hashlib.sha1(candidate.encode()).hexdigest()
            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
    print("Done with Single word + 4 digit")


# Single word + 5 digits
def method_word_plus_5_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    for word in words:
        for i in range(100000):
            candidate = f"{word}{i:05d}"
            computed_hash = hashlib.sha1(candidate.encode()).hexdigest()
            if computed_hash in hashes_map:
                match_num = hashes_map[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
    print("Done with Single word + 5 digit")


# ===========================
remaining = {
    "ca1f7fef6f7a839c083e96f77ac7cf3991323af7": 12,
    "08958bb5e582136f7b4cc32bdbe9b23603613d1a": 14,
    "177080c8b8f44ea62c1a4baeeeb726ac1f9985ae": 15,
    "808543b37169708c597e23c7adbe743be8e05ad7": 16,
    "65abe9e1efbd6efbdf3d6ea3c4c2f6c0325cbb68": 19,
    "13de3541c0564ee2267e37a85045a615476cfa03": 20,
}


# 2 word combination
def method_word_plus_word():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    remaining = {
        "ca1f7fef6f7a839c083e96f77ac7cf3991323af7": 12,
        "08958bb5e582136f7b4cc32bdbe9b23603613d1a": 14,
        "177080c8b8f44ea62c1a4baeeeb726ac1f9985ae": 15,
        "808543b37169708c597e23c7adbe743be8e05ad7": 16,
        "65abe9e1efbd6efbdf3d6ea3c4c2f6c0325cbb68": 19,
        "13de3541c0564ee2267e37a85045a615476cfa03": 20,
    }

    for word1 in words:
        hash1 = hashlib.sha1(word1.encode())  # hash w1 Once, and we can reuse it

        for word2 in words:
            if len(word1) + len(word2) > 20:
                continue  # skip max length

            hash2 = hash1.copy()  # restore checkpoint after word1
            hash2.update(word2.encode())  # only process word 2's bytes from here
            computed_hash = hash2.hexdigest()

            if computed_hash in remaining:
                candidate = f"{word1}{word2}"
                match_num = remaining[computed_hash]
                print(f"Match found: Hash #{match_num} {candidate} -> {computed_hash}")
                del remaining[computed_hash]  # stop checking this one once found

            if not remaining:
                break  # everything's cracked, no need to keep going

    print("Finished 2 word combination")


def two_word_combo_plus_single_digit():
    with open("dictionary.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]

    remaining = {
        "ca1f7fef6f7a839c083e96f77ac7cf3991323af7": 12,
        "808543b37169708c597e23c7adbe743be8e05ad7": 16,
        "13de3541c0564ee2267e37a85045a615476cfa03": 20,
    }

    attempt_count = 0

    for word1 in words:
        hash1 = hashlib.sha1(word1.encode())

        for word2 in words:
            base_len = len(word1) + len(word2)
            if base_len + 1 > 20:
                continue

            hash_word1_word2 = hash1.copy()
            hash_word1_word2.update(word2.encode())

            for i in range(10):
                attempt_count += 1
                if attempt_count % 1_000_000 == 0:
                    print(f"Checked {attempt_count:,} combinations so far")

                num_str = str(i)
                hash_final = hash_word1_word2.copy()
                hash_final.update(num_str.encode())
                computed_hash = hash_final.hexdigest()

                if computed_hash in remaining:
                    candidate = f"{word1}{word2}{num_str}"
                    print(
                        f"Match found: Hash #{remaining[computed_hash]} {candidate} -> {computed_hash}"
                    )
                    del remaining[computed_hash]

                if not remaining:
                    print("All targeted hashes found.")
                    return

    print(f"Finished 2-word + single-digit pass. Still unsolved: {remaining}")


if __name__ == "__main__":
    # === Single word hash ===
    ### method_1()
    # Match found: Hash #10 triumphant -> d1808c6fc5dd939a1889da7c11f68bdb10b727b7
    # Match found: Hash #6 monday -> ad8167df4b75bd9f2e165ea9f6053195cf7652b5
    # Match found: Hash #13 bewildered -> 39fb6e0d23f83a4e016c0f725dda9050b72af4a2

    # === Just numbers ==
    ### method_1_digit()
    # no result
    ### method_2_digit()
    # no result
    ### method_3_digit()
    # Match found: Hash #5 000 -> 8aefb06c426e07a0a671a1e2488b4858d694a730
    ### method_4_digit()
    # no result
    ### method_5_digit()
    # no result
    ### method_6_digit()
    # Match found: Hash #1 123456 -> 7c4a8d09ca3762af61e59520943dc26494f8941b
    # Match found: Hash #2 987654 -> dea742e166979027ae70b28e0a9006fb1010e760
    ### method_7_digit()
    # no result
    ### method_8_digit()
    # Match found: Hash #3 20240501 -> 789d1dd349b28fcdb61da280d58c0df721da9143
    # method_9_digit()
    # Match found: Hash #8 000000009 -> 754f1d6a31e8fcfc30cf8257d9e035a92a11b328
    ### method_10_digit()
    # Match found: Hash #7 5013974000 -> ea074a4e069fdd30468ad32019334091cd6f2545

    # Single Word + Number
    ### method_word_plus_1_digit()
    # Match found: Hash #11 convince0 -> b7c71d5a119e91a42a9abd1fcb02692a28c404d4
    ### method_word_plus_2_digit()
    # no result
    ### method_word_plus_3_digit()
    # Match found: Hash #9 writings784 -> 1db7b321af0e8d0da63277a9d0bc67a176b03ed8
    # Match found: Hash #17 aid123 -> 9a4b9040cb885c4c25db1d821a2cec35c11cd636
    ### method_word_plus_4_digit()
    # Match found: Hash #4 marching2024 -> f122778ac920da565c668acc6c0a247edd6adb27
    ### method_word_plus_5_digit()
    # Match found: Hash #18 demonstration99999 -> 925184f33c2cb6f0bb7abdfeef317001d2569051

    # === All matches found so far ===
    # Match found: Hash #1 123456 -> 7c4a8d09ca3762af61e59520943dc26494f8941b
    # Match found: Hash #2 987654 -> dea742e166979027ae70b28e0a9006fb1010e760
    # Match found: Hash #3 20240501 -> 789d1dd349b28fcdb61da280d58c0df721da9143
    # Match found: Hash #4 marching2024 -> f122778ac920da565c668acc6c0a247edd6adb27
    # Match found: Hash #5 000 -> 8aefb06c426e07a0a671a1e2488b4858d694a730
    # Match found: Hash #6 monday -> ad8167df4b75bd9f2e165ea9f6053195cf7652b5
    # Match found: Hash #7 5013974000 -> ea074a4e069fdd30468ad32019334091cd6f2545
    # Match found: Hash #8 000000009 -> 754f1d6a31e8fcfc30cf8257d9e035a92a11b328
    # Match found: Hash #9 writings784 -> 1db7b321af0e8d0da63277a9d0bc67a176b03ed8
    # Match found: Hash #10 triumphant -> d1808c6fc5dd939a1889da7c11f68bdb10b727b7
    # Match found: Hash #11 convince0 -> b7c71d5a119e91a42a9abd1fcb02692a28c404d4
    # Match found: Hash #13 bewildered -> 39fb6e0d23f83a4e016c0f725dda9050b72af4a2
    # Match found: Hash #17 aid123 -> 9a4b9040cb885c4c25db1d821a2cec35c11cd636
    # Match found: Hash #18 demonstration99999 -> 925184f33c2cb6f0bb7abdfeef317001d2569051

    # 2 word combination
    ### method_word_plus_word()
    # Match found: Hash #15 bestrings -> 177080c8b8f44ea62c1a4baeeeb726ac1f9985ae
    # Match found: Hash #19 investigationsaving -> 65abe9e1efbd6efbdf3d6ea3c4c2f6c0325cbb68
    # Match found: Hash #14 excitephysician -> 08958bb5e582136f7b4cc32bdbe9b23603613d1a

    # 2 word combo plus 1 digit
    # two_word_combo_plus_single_digit()
    # Match found: Hash #20 jerrysay8 -> 13de3541c0564ee2267e37a85045a615476cfa03
    # Finished 2-word + single-digit pass. Still unsolved: {'ca1f7fef6f7a839c083e96f77ac7cf3991323af7': 12, '808543b37169708c597e23c7adbe743be8e05ad7': 16}

    # Hashes left: 16 and 20, likely 3 word combos
    pass
