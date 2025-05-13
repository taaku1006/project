class ValidationError(Exception):
    """バリデーションエラー用の例外"""
    pass

def validate_user_data(name: str, email: str):
    if not name or not email:
        raise ValidationError("すべてのフィールドを入力してください")
    if "@" not in email:
        raise ValidationError("有効なメールアドレスを入力してください")
