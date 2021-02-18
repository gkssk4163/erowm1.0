// 랜덤 패스워드 생성
function generateRandomPassword(digit) {
	return Math.random().toString(36).substr(2, digit)
}
