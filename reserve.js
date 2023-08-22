// 予約を登録するJavaScript関数
function registerReservation() {
    if (selectedTime) {
        const selectedValue = document.querySelector(`input[name='reservation']:checked`).value;
        const [time, numPeople] = selectedValue.split('-');
        alert(`選択された時間: ${time}, 人数: ${numPeople}`);
        // ここに予約をサーバーに送信するロジックを追加できます
    } else {
        alert('時間を選択してください。');
    }
}