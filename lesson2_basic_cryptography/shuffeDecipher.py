def analyze_letter_frequency(text):
    """
    Analyzes the given text and returns the most and least common letters.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        tuple: (most_common_letters, least_common_letters, frequency_dict)
            - most_common_letters: list of most frequent letters
            - least_common_letters: list of least frequent letters
            - frequency_dict: dictionary with all letter frequencies
    """
    # Convert text to lowercase and filter out non-alphabetic characters
    text = ''.join(char for char in text.lower() if char.isalpha())
    
    if not text:
        return ([], [], {})
    
    # Count letter frequencies
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Find the highest and lowest frequencies
    if not frequency:
        return ([], [], {})
    
    max_freq = max(frequency.values())
    min_freq = min(frequency.values())
    
    # Get letters with highest and lowest frequencies
    most_common = [char for char, count in frequency.items() if count == max_freq]
    least_common = [char for char, count in frequency.items() if count == min_freq]
    
    return (most_common, least_common, frequency)

def display_letter_frequency(text):
    """
    Analyzes and displays the letter frequency information for the given text.
    
    Args:
        text (str): The text to analyze
    """
    most_common, least_common, freq_dict = analyze_letter_frequency(text)
    
    if not freq_dict:
        print("No letters found in the text.")
        return
    
    # Sort the frequency dictionary for display
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    print(f"Letter frequency analysis of text ({len(text)} characters, {sum(freq_dict.values())} letters):")
    print("\nFull frequency list (most to least common):")
    for char, count in sorted_freq:
        percentage = (count / sum(freq_dict.values())) * 100
        print(f"'{char}': {count} occurrences ({percentage:.2f}%)")
    
    print("\nMost common letter(s):")
    for char in most_common:
        percentage = (freq_dict[char] / sum(freq_dict.values())) * 100
        print(f"'{char}': {freq_dict[char]} occurrences ({percentage:.2f}%)")
    
    print("\nLeast common letter(s):")
    for char in least_common:
        percentage = (freq_dict[char] / sum(freq_dict.values())) * 100
        print(f"'{char}': {freq_dict[char]} occurrences ({percentage:.2f}%)")

# Example usage
if __name__ == "__main__":
    sample_text = """
    hm al, mo tmh hm al, huvh gn hul jzlnhgmt:
qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo
hul nxgtsn vty voomqn mr mzhovslmzn rmohztl,
mo hm hvel vocn vsvgtnh v nlv mr homzaxln
vty ak mppmngts lty hulc?
hm ygl: hm nxllp;
tm cmol; vty, ak v nxllp hm nvk ql lty
hul ulvoh-vwul vty hul humznvty tvhzovx numwen
huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt
yldmzhxk hm al qgnu'y. hm ygl, hm nxllp;
hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza;
rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl
qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,
cznh sgdl zn pvznl
  
    """
    display_letter_frequency(sample_text)