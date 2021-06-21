def radixSort(nums):
    # 가장 먼저 최대값이 얼마인지를 찾습니다.
    maximum = max(nums)
    max_n_digits = len(str(maximum))
     
    # 1의 자리부터 각 자리마다 counting sort를 시행합니다.
    result = nums
    for i in xrange(max_n_digits):
        result = countingSort(result, i, 10)
         
    return result

def countingSort(nums, digit_index, base):
    # 먼저 base만큼의 list들의 list를 생성해 줍니다.
    # 예를 들면 주어진 수들이 해당 자리수에 어떤 숫자들이 있느냐에 따라 각 리스트로 분배될 것입니다.
    buckets = [[] for _ in xrange(base)]
     
    for n in nums:
        # 각 숫자마다 돌면서 digit_index번째 자리수를 구하고, bucket에 집어넣습니다.
        digit = (n / (base**digit_index)) % base
        buckets[digit].append(n)
     
    # 최종적으로 그 bucket을 순차적으로 돌면서 결과 리스트에 넣으면 됩니다.
    result = []
    for b in buckets:
        for n in b:
            result.append(n)
     
    return result

#https://smlee729.wordpress.com/2018/03/11/radix-sort/