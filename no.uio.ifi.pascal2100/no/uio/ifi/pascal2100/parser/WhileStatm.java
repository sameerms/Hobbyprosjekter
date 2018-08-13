package no.uio.ifi.pascal2100.parser;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.*;
class WhileStatm extends Statement {
	
Expression expr;
Statement body;

	WhileStatm(int lNum) {
		super(lNum);
			}


	@Override public String identify() {
		return "<while-statm> on line " + lineNum;
								}
	public static WhileStatm parse(Scanner s) {
		enterParser("while-statm");
		WhileStatm ws = new WhileStatm(s.curLineNum());
		s.skip(whileToken);
		ws.expr = Expression.parse(s);
		s.skip(doToken);
		ws.body = Statement.parse(s);
		leaveParser("while-statm");
		return ws;
		}
	
	@Override void prettyPrint() {
	Main.log.prettyPrint("while "); expr.prettyPrint();
	Main.log.prettyPrintLn(" do"); Main.log.prettyIndent();
	body.prettyPrint(); Main.log.prettyOutdent();
	}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		expr.check(curScope, lib);
		body.check(curScope, lib);
	}
}
