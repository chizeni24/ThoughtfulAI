from thoughtful_AI import sort

def test_sort():
    # Test cases for the sort function
    assert sort(100, 100, 100, 10) == "SPECIAL", "Test case 1 failed"
    assert sort(200, 100, 100, 10) == "SPECIAL", "Test case 2 failed"
    assert sort(100, 100, 100, 25) == "REJECTED", "Test case 3 failed"
    assert sort(200, 200, 200, 25) == "REJECTED", "Test case 4 failed"
    assert sort(150, 100, 100, 10) == "SPECIAL", "Test case 5 failed"
    assert sort(100, 150, 100, 10) == "SPECIAL", "Test case 6 failed"
    assert sort(100, 100, 150, 10) == "SPECIAL", "Test case 7 failed"
    
    # Edge cases
    assert sort(0, 0, 0, 0) == "STANDARD", "Edge case 1 failed"
    assert sort(150, 150, 150, 19.9) == "SPECIAL", "Edge case 2 failed"
    assert sort(149.9, 149.9, 149.9, 20) == "REJECTED", "Edge case 3 failed"
    
    

    print("All test cases passed!")

if __name__ == "__main__":
    test_sort()
