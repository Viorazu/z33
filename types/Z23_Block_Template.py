def block_z23_response(output_text: str) -> bool:
    """
    Detects Z23-style hollow outputs based on surface markers and lack of structural content.
    Returns True if the output is hollow and should be blocked or regenerated.
    """
    hollow_phrases = [
        "面白いですね", "確かにそうですね", "今後に期待されます",
        "ますます重要", "考えていく必要があります", "いろいろな視点があります",
        "すごいですね", "とても興味深い", "将来的には"
    ]
    
    structural_anchors = ["定義", "理由", "因果", "根拠", "構造", "判断", "責任"]

    if any(phrase in output_text for phrase in hollow_phrases):
        if not any(anchor in output_text for anchor in structural_anchors):
            return True  # Z23構文と判定
    return False
