package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class TermOperator extends Operator {

	public SimpleExp smpex;
	String symbol;
	static TermOperator tot = null;

	public TermOperator(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	public static TermOperator parse(Scanner s) {
		
			enterParser("term opr");
			
			TermOperator localTmOpr = new TermOperator(s.curLineNum());
			localTmOpr.oprToken = s.curToken.kind;
			s.readNextToken();
			
			leaveParser("term opr");
			return localTmOpr;
			}
		
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<term opr> "+symbol  + " on line " + lineNum;
	}
		@Override
		void prettyPrint() {
			// TODO Auto-generated method stub
			String op= "";
			
			/*System.out.println("term oper token called");*/
			switch (oprToken) {
			
			case addToken:    op = "+";  break;
			case subtractToken:      op = "-";   break;
			case orToken: op = "or";  break;
			}
			Main.log.prettyPrint(" " + op + " ");
	}

		@Override
		public void check(Block curScope, Library lib) {
			// TODO Auto-generated method stub
			
		}

	}