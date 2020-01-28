def dice(first, second, third):
    equal = int(first == second == third)
    single_equal = int(first == second) * int(not equal)
    single_equal_ = int(first == third) * int(not equal)
    single_equal__ = int(second == third) * int(not equal)
    return (10000 * equal) + (first * 1000) * equal + (1000 * single_equal) + (first * 100) * single_equal + (1000 * single_equal_) + (first * 100) * single_equal_ + (1000 * single_equal__) + (second * 100) * single_equal__ + max([first, second, third]) * 100 * abs(single_equal + single_equal_ + single_equal__ + equal - 1)

if __name__ == '__main__':
    first, second, third = map(int, input().split())
    print(dice(first, second, third))
