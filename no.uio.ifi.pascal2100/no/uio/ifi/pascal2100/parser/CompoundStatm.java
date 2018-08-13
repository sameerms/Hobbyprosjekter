package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.commaToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.leftParToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.nameToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class CompoundStatm extends Statement {

	StatmList stmt;
	public CompoundStatm(int lNum) {
		super(lNum);
		// TODO Auto-generated constructor stub
	}

	@Override public String identify() {
		return "<compound statm> on line " + lineNum;
								}
	
	
	/**
     * Parse a CompoundStatm.
     * @param Scanner Tokens.
     * @return the CompoundStatm object of the parse tree.
     * --begin --statm list---- end--
     */
	public static CompoundStatm parse(Scanner s) {
		enterParser("compound statm");
	
			s.skip(beginToken);
			CompoundStatm cs= new CompoundStatm(s.curLineNum());
		
		
			cs.stmt=StatmList.parse(s);cs.stmt.compnd=cs;
			
			s.skip(endToken);
			
		
			leaveParser("compound statm");
			return cs;
		}
	
@Override void prettyPrint() {


Main.log.prettyPrint("begin");
Main.log.prettyIndent();
stmt.prettyPrint();
Main.log.prettyOutdent();
Main.log.prettyPrint("end");

}

@Override
public void check(Block curScope, Library lib) {
	// TODO Auto-generated method stub
	if (stmt != null) stmt.check(curScope, lib);
}
}