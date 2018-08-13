package no.uio.ifi.pascal2100.parser;
import no.uio.ifi.pascal2100.scanner.*;
import no.uio.ifi.pascal2100.main.*;
import java.util.EnumSet;

public abstract class PascalSyntax {
	public int lineNum;
	public TokenKind curTok;
	public TokenKind NextTok;
	public static int numberliteral = 0;
	PascalSyntax(int n) {
		lineNum = n;
	}
	PascalSyntax() {
		
	}

	boolean isInLibrary() {
		return lineNum < 0;
	}

	 public abstract void check(Block curScope, Library lib);
	// Del 4: abstract void genCode(CodeFile f);
	abstract public String identify();

	abstract void prettyPrint();

	void error(String message) {
		Main.error("Error at line " + lineNum + ": " + message);
	}

	static void enterParser(String nonTerm) {
		Main.log.enterParser(nonTerm);
		/*Main.log.noteParserInfo(nonTerm);
		Main.log.prettyPrint(nonTerm);*/
		
		
	}

	static void leaveParser(String nonTerm) {
		Main.log.leaveParser(nonTerm);
	}

	
}
