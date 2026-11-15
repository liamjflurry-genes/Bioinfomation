k = int(input("Enter the number of homozygous dominant individuals (k): "))
m = int(input("Enter the number of heterozygous individuals (m): "))
n = int(input("Enter the number of homozygous recessive individuals (n): "))

def dominant_offspring_prob(k, m, n):
    total = k + m + n
    
    # Calculate the probability of each pairing producing a recessive (aa) child
    recessive_recessive = (n / total) * ((n - 1) / (total - 1)) * 1.0
    hetero_hetero       = (m / total) * ((m - 1) / (total - 1)) * 0.25
    hetero_recessive    = 2 * (m / total) * (n / (total - 1)) * 0.50
    
    # Total probability of a purely recessive (aa) offspring
    prob_recessive = recessive_recessive + hetero_hetero + hetero_recessive
    
    # Subtract from 1 to get the probability of at least one dominant allele
    return 1 - prob_recessive

result = dominant_offspring_prob(k, m, n)
print(f"{result:.5f}")
