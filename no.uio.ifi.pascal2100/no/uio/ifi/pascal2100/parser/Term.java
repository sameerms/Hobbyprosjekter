package no.uio.ifi.pascal2100.parser;

import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class Term extends PascalSyntax {

	public SimpleExp smpexp;
	public  Factor ft1 = null;
	public  Factor ft2;
	CharLiteral c;
	FactorOperator ftOp;
	 
	public Term nextTerm;
	public static List <FactorOperator>factoroprlist = new ArrayList<FactorOperator>(); 
	public static List <Factor>factorlist = new ArrayList<Factor>(); 

	public Term(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}


	public static Term parse(Scanner s) {
		
			enterParser("term");
			Term t = new Term(s.curLineNum());
			
			
			t.ft1=Factor.parse(s);
			factorlist.add(t.ft1);
			
			while(s.curToken.kind.isFactorOpr()){
				t.ftOp=FactorOperator.parse(s); 
				factoroprlist.add(t.ftOp); 
				s.readNextToken();
				t.ft2=Factor.parse(s);
				
				factorlist.add(t.ft2); 
			}
			
			leaveParser("term");
			return t;
			}
	
	
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<term > "+ " on line " + lineNum;
	}
		
		@Override
		void prettyPrint() {
			if(ft1!=null) ft1.prettyPrint();
			if(ftOp!=null){
				ftOp.prettyPrint();
				if(ft2!=null)ft2.prettyPrint();
			}
		}


		@Override
		public void check(Block curScope, Library lib) {
			// TODO Auto-generated method stub
			if(ft1!=null) ft1.check(curScope, lib);
			if(ftOp!=null){
				ftOp.check(curScope, lib);
				if(ft2!=null)ft2.check(curScope, lib);
			}
		}

	}
