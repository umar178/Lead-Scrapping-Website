# don't edit this code, don't run this either \\Umar
import time

from flask import Flask, render_template, request, redirect, url_for, send_file
import subprocess
import os
import csv

app = Flask(__name__)
show_table = False


@app.route("/", methods=["GET"])
def render_home():
    global show_table
    if show_table:
        CSV_FILE = 'google-maps-scraper\\outputs\\output.csv'
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        show_table = False
        return render_template("index.html", rows=rows, show_table=True)
    else:
        return render_template("index.html", show_table=False)


@app.route('/Details')
def details():
    return render_template('Details.html')


def format_csv():
    input_file = 'google-maps-scraper\\outputs\\result.csv'  # Path to existing CSV file
    output_file = 'google-maps-scraper\\outputs\\output.csv'  # Path to the new CSV file
    required_columns = ['title', 'category', 'address', 'website', 'phone', 'emails']

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)  # Read the CSV file as a dictionary (key-value pairs)
        writer = csv.DictWriter(outfile, fieldnames=required_columns)

        writer.writeheader()  # Write the header to the new CSV

        # Iterate through each row in the original CSV file
        for row in reader:
            # Filter out the required columns and write them to the new CSV
            filtered_row = {key: row[key] for key in required_columns if key in row}
            writer.writerow(filtered_row)


@app.route("/", methods=["POST"])
def process_form():
    global show_table
    category = request.form.get("category")
    location = request.form.get("location")
    timeout = request.form.get("timeout")

    if category and location and timeout:
        input_text = category + " in " + location
        print(input_text)

        with open('google-maps-scraper\\example-queries.txt', 'w') as file:
            file.write(input_text)

        prompt = (
                'cmd.exe /K "cd google-maps-scraper && '
                'google-maps-scraper -input example-queries.txt -results outputs\\result.csv '
                '-exit-on-inactivity ' + timeout + 'm -email"'
        )
        print(prompt)

        try:
            process = subprocess.Popen(
                prompt,
                cwd=os.getcwd(),
                shell=True
            )
            print("execution Started")
            time.sleep((int(timeout) * 60) + 20)
            process.terminate()
            print("execution ended")
            format_csv()
            show_table = True
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Category or location was not provided.")

    return redirect(url_for('render_home'))


@app.route("/download")
def download_csv():
    CSV_FILE = 'google-maps-scraper\\outputs\\output.csv'
    try:
        return send_file(CSV_FILE, as_attachment=True)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
