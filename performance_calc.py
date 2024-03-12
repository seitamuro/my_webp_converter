import json
import sys

def extract_performance_data(json_file):
    # JSONファイルを読み込む
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # 必要なパフォーマンス指標を取得
    performance_data = {
        'FCP': data['audits']['first-contentful-paint']['numericValue'],
        'SI': data['audits']['speed-index']['numericValue'],
        'FMP': data['audits']['first-meaningful-paint']['numericValue'],
        'TTI': data['audits']['interactive']['numericValue'],
        'LCP': data['audits']['largest-contentful-paint']['numericValue'],
        'TBT': data['audits']['total-blocking-time']['numericValue'],
        'CLS': data['audits']['cumulative-layout-shift']['numericValue']
    }
    
    return performance_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <lighthouse_json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    performance_data = extract_performance_data(json_file)
    for metric in performance_data:
        print(f"{metric}: {performance_data[metric]}")

