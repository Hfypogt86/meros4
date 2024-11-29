# حفظ الملاحظات إلى ملف JSON
@app.route('/save-notes', methods=['POST'])
def save_notes():
    try:
        new_notes = request.get_json()
        with open(notes_file, 'w') as f:
            json.dump(new_notes, f)
        return jsonify({'message': 'Notes saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
