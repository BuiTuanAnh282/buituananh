import json
import math

file = 'alexa-top-1m.csv'

def bigrams(input_list):
    # Nhận danh sách input_list và trả về các cặp tuần tự gồm hai phần tử liên tiếp trong danh sách.
    return zip(input_list, input_list[1:])

# Tạo một từ điển trống để lưu trữ cặp ký tự và số lần xuất hiện của chúng.
pairs = {}
line_count = 0

# Mở tệp tin 'alexa-top-1m.csv' dưới chế độ đọc và đặt tệp tin vào biến fi.
with open(file, 'r') as fi:
    # Lặp qua từng dòng trong tệp tin.
    for line in fi:
        # Tăng biến line_count lên 1 để theo dõi số dòng đã đọc.
        line_count += 1

        # Tách dòng thành các phần tử bằng dấu phẩy và lưu vào danh sách arr.
        arr = line.split(',')
        ranking = arr[0]

        # Lấy phần đầu tiên (trước dấu chấm) của phần tử thứ hai trong danh sách arr và lưu vào biến basedomain. Đây là phần tên miền gốc của trang web.
        basedomain = arr[1].split('.')[0]

        # Tách basedomain thành các từ riêng biệt bằng dấu gạch ngang và lưu vào danh sách words.
        words = basedomain.split('-')

        # Lặp qua từng từ trong danh sách words.
        for word in words:
            #  Kiểm tra nếu độ dài của từ lớn hơn 1.
            if len(word) > 1:
                # Gọi hàm bigrams để tạo ra các cặp ký tự từ từ hiện tại và lưu vào biến b.
                b = bigrams(word)

                # Lặp qua từng cặp ký tự trong biến b. 
                for char_tuple in b:
                    # Ghép hai ký tự trong cặp thành một cặp ký tự và lưu vào biến pair
                    pair = char_tuple[0] + char_tuple[1]
                    # Kiểm tra nếu cặp ký tự đã tồn tại trong từ điển pairs.
                    if pair in pairs:
                        # Tăng giá trị của cặp ký tự trong từ điển pairs lên 1.
                        pairs[pair] += 1
                    else:
                        pairs[pair] = 1

# Tính tổng số lần xuất hiện của tất cả các cặp ký tự trong từ điển pairs và lưu vào biến total_pairs.
total_pairs = sum(pairs.values())
print(total_pairs)

# Lặp qua từng cặp key-value trong từ điển pairs.
for k, v in pairs.items():
    # Tính xác suất xuất hiện của cặp ký tự bằng cách chia số lần xuất hiện của cặp đó cho tổng số lần xuất hiện của tất cả các cặp ký tự.
    probability = float(v) / total_pairs
    # Cập nhật giá trị của cặp ký tự trong từ điển pairs thành một từ điển con chứa số lần xuất hiện, xác suất và giá trị logarithm của xác suất.
    pairs[k] = {
        'count': v,
        'probability': probability,
        'log': round(math.log10(probability), 5)
    }

# Thêm giá trị total_pairsvào từ điểnpairsvới khóa là'total_pairs'`. Điều này hữu ích để tính toán số lần xuất hiện của các cặp ký tự sau này.
pairs['total_pairs'] = total_pairs

# Chuyển đổi từ điển pairs thành chuỗi JSON bằng cách sử dụng hàm json.dumps().
j = json.dumps(pairs)

# Mở tệp tin 'character_pair_probabilities.json' dưới chế độ ghi và đặt tệp tin vào biến fo.
with open('character_pair_probabilities.json', 'w') as fo:
    # Ghi chuỗi JSON j vào tệp tin.
    fo.write(j)

exit()