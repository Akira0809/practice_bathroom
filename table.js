// 選択されたラジオボタンの時間を格納する変数
let selectedTime = null;

function selectTime(time) {
    selectedTime = time;
}

for (let i = 16; i < 22; i++) {
    for (let j = 0; j < 60; j += 30) {
        const time = `${i.toString().padStart(2, '0')}:${j.toString().padStart(2, '0')}`;
        document.write(`
            <tr>
                <td>${time}</td>
                <td><input type='radio' name='reservation' value='${time}-4人' onclick="selectTime('${time}')"></td>
                <td><input type='radio' name='reservation' value='${time}-9人' onclick="selectTime('${time}')"></td>
            </tr>
        `);
    }
}